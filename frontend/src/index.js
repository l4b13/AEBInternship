import React, {createContext} from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import UserSite from "./site/UserSite";

export const Context = createContext(null)

ReactDOM.render(
    <Context.Provider value={{
        user: new UserSite(),
    }}>
        <App />
    </Context.Provider>,
    document.getElementById('root')
);



