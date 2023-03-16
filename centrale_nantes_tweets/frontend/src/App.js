import React, { useState, useEffect } from "react";
import "./App.css";
import upvoteIcon from "./upvote.svg"; // Import upvote icon
import downvoteIcon from "./downvote.svg"; // Import downvote icon

function App() {
  const [posts, setPosts] = useState([]);

  useEffect(() => {
    const fetchPosts = async () => {
      const response = await fetch("http://localhost:8000/api/posts/");
      
      if (response.status === 200) {
        const data = await response.json();
        setPosts(data);
      } else {
        console.error("Failed to fetch data:", response.status);
      }
    };
    fetchPosts();
  }, []);

  return (
    <div className="App">
      <h1>Latest Posts from /r/docker</h1>
      <ul className="post-list">
        {posts.map((post) => (
          <li key={post.id} className="post-item">
            <div className="post-votes">
              <img src={upvoteIcon} alt="Upvote" className="vote-icon" />
              <span>{post.ups}</span>
              <img src={downvoteIcon} alt="Downvote" className="vote-icon" />
              <span>{post.downs}</span>
            </div>
            <a href={`https://www.reddit.com${post.permalink}`} target="_blank" rel="noreferrer">
              {post.title}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
