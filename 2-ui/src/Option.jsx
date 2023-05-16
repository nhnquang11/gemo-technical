import translation from "./translation"
import { useContext, useState } from 'react';
import { LangContext } from './LangContext';


function Option({ option, item, setUnitPrice }) {
    const { lang } = useContext(LangContext)
    const selection = option.select;
    const optionNames = Object.keys(selection)
    const defaultOpt = optionNames[0]
    const [currOpt, setCurrOpt] = useState(`${item.name}-${option.name}-${defaultOpt}`)
    const [price, setPrice] = useState(selection[defaultOpt])
    const handleOnChange = (event) => {
        const diff = event.target.value - price;
        setCurrOpt(event.target.id)
        setPrice(event.target.value);
        setUnitPrice(prev =>  prev + diff)
    }

    return (
        <div className="flex flex-col items-start">
            { /* Option title */ }
            <h1 className="font-medium mb-1">{translation[lang][option.name]}</h1>
            { /* Option content */ }
            {
                optionNames.map(optName => {
                       const opt = 
                       <div className="flex flex-row mb-2">
                        <input onChange={handleOnChange} checked={`${item.name}-${option.name}-${optName}` === currOpt} name={option.name} type="radio" value={selection[optName]} id={`${item.name}-${option.name}-${optName}`}/>
                        <label className="ml-1 text-xs font-light font-mono" for={`${item.name}-${option.name}-${optName}`}>{translation[lang][optName]} (${selection[optName]})</label>
                       </div>
                       return opt
                    }
                )
            }
        </div>
    )
}

export default Option