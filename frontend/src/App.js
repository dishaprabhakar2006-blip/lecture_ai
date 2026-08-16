import React,{useState} from 'react';
import axios from 'axios';
import './App.css';
import ReactMarkdown from 'react-markdown';

function App(){
  const[url,setUrl]=useState('');
  const[loading,setLoading]=useState(false);
  const[result,setResult]=useState(null);
  const[question,setQuestion]=useState('');
  const[answer,setAnswer]=useState('');
  const[activeTab,setActiveTab]=useState('notes');

  const handleSubmit=async ()=>{
    if (!url) return;
    setLoading(true);
    try {
      const response =await axios.post('http://localhost:8000/transcribe',{url});
      setResult(response.data);
    } catch (error){
      alert('Error processing video. Please try again.');
    }
    setLoading(false);
  };
  const handleChat=async ()=>{
    if (!question) return;
    try {
      const response = await axios.post('http://localhost:8000/chat', {
        video_url: url,
        question: question
    });
    setAnswer(response.data.answer);
  } catch (error) {
    alert('Error getting answer.');
  }
    
  };
  return (
    <div className="app">
      <h1>🎓 Lecture AI</h1>
      <p>Turn any Youtube lecture into study materials</p>

      <div className="input-section">
        <input
        type="text"
        placeholder="Paste Youtube URL here..."
        value={url}
        onChange={(e) => setUrl(e.target.value)}
        />
        <button onClick={handleSubmit} disabled={loading}>
          {loading ? 'Processing...':'Generate Study Materials'}
          </button>
          </div>
          {loading && <p className="loading">⏳ This may take 2-3 minutes for long videos...</p>}
          {result && (
            <div className="result-section">
              <div className="tabs">
                <button onClick={() => setActiveTab('notes')} className={activeTab === 'notes'? 'active':''}>Notes</button>
                <button onClick={() => setActiveTab('summary')} className={activeTab === 'summary'? 'active':''}>Summary</button>
                <button onClick={() => setActiveTab('mcqs')} className={activeTab === 'mcqs'? 'active':''}>MCQs</button>
                <button onClick={() => setActiveTab('flashcards')} className={activeTab === 'flashcards'? 'active':''}>Flashcards</button>
                <button onClick={() => setActiveTab('chat')} className={activeTab === 'chat'? 'active':''}>Chat</button>
                </div>

                <div className="tab-content">
                  {activeTab === 'notes' && <ReactMarkdown>{result.notes}</ReactMarkdown>}
                  {activeTab === 'summary' && <ReactMarkdown>{result.summary}</ReactMarkdown>}
                  {activeTab === 'mcqs' && <ReactMarkdown>{result.mcqs}</ReactMarkdown>}
                  {activeTab === 'flashcards' && <ReactMarkdown>{result.flashcards}</ReactMarkdown>}
                  {activeTab === 'chat'&& (
                    <div className="chat-section">
  <input
  type="text"
  placeholder="Ask a question about this lecture..."
  value={question}
  onChange={(e) => setQuestion(e.target.value)}
  style={{width:'100%'}}
  />
  <button onClick={handleChat}>Ask</button>
  {answer && <div className="answer"><ReactMarkdown>{answer}</ReactMarkdown></div>}
</div>
                      )}
                      </div>
                      </div>
                      )}
                      </div>
  );
}
export default App;