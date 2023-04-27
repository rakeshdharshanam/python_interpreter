import React from 'react'
import { useState } from 'react'
import axios from "axios"
import "./index.css" 
import python_image from "./Python-image.png"



function Js_code(){
    // const python_code = useRef()
    const [code,setcode] = useState()
    const [output,setoutput] = useState()

    function run(){
        const payload = {
            language : "javascript",
            
            code
        };
        // axios.get("http://127.0.0.1:5000/home").then(resp=>console.log(resp))
        // var data = JSON.stringify(payload)
        // data = JSON.parse(data)
        axios.post("http://127.0.0.1:5000/js",payload).then(resp=>setoutput(resp.data))
        // var code_output = 
        // console.log(resp.data)
        // setoutput(resp.data)
        // console.log(typeof(payload))
    }

    return(
        <div> 
            <p>start typing javascript:</p>
            <textarea value={code} onChange={(e)=> setcode(e.target.value)} id='ta1'/>
            <p id='p2'>here is your output:</p>
            <textarea id='ta2'  value={output}/>
            <button onClick={run}>Run</button>
        </div>
    )
}

export default Js_code