import './App.css';
import Python_code from './Python_code';
import Js_code from './Js_code';
import Navbar from './Navbar';

function App() {

  let pathname = window.location.pathname
  console.log(pathname)
  let Component 
  if(pathname ==="/js"){
    Component = <Js_code/>
  }
  else{
    Component = <Python_code/>
  }

  return (
    <div>
      <Navbar/>
      {Component}
    </div>
  );
}

export default App;
