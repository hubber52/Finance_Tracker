import { useState, useContext } from 'react';
import axios from 'axios';
import {useNavigate} from 'react-router-dom';
import { APIContext } from '../Contexts/APIContext';

import "../Styles/Pages/landing.css";

const Register = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [email, setEmail] = useState('');
    const [responseMessage, setResponseMessage] = useState('');
    const navigate = useNavigate();
    const url = useContext(APIContext);
    
    const handleSubmit = async (e : any) => {
        e.preventDefault();

    // API call to register a user
        try {
          const response = await axios.post(url+'register/', {"username":username, "password":password, "email":email});
          setResponseMessage('Post created successfully!');
          console.log('Response:', response.data);
          if(!window.confirm('Account creation successful, please log in')) return;
          navigate('/login')
        } 
        catch (error) {
          setResponseMessage('Error creating post.');
          console.error('Error:', error);
          if (!window.confirm('Please try another username')) return;
        }
    console.log('Username:', {username}, 'Password:', {password});
    };

    return (
        <div className="landing">
            <button className="login-button" onClick = {() => navigate('/')}> Back </button>
            <div className="landing-header"> Register for a new account </div>
            <form onSubmit={handleSubmit}>
                <div>
                    <label htmlFor="username">Username:</label>
                        <input
                            type="username"
                            id="username"
                            value={username}
                            onChange={(e) => setUsername(e.target.value)}
                        />
                </div>
                <div>
                    <label htmlFor="password">Password:</label>
                        <input
                            type="password"
                            id="password"
                            value={password}
                            onChange={(e) => setPassword(e.target.value)}
                    />
                </div>
                <div>
                    <label htmlFor="email">Email</label>
                        <input
                        type = "email"
                        id = "email"
                        value = {email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                </div>
                <button className="register-button" type="submit">Sign Up</button>
 
            </form>
            <button className="login-button" onClick = {() => navigate('/login')}> Login</button>
        </div>
    );
};

export default Register;