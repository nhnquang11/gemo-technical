import translation from "./translation"
import { useContext, useState } from 'react';
import { LangContext } from './LangContext';
import Option from "./Option";


function ItemOrder({item}) {
    const { lang } = useContext(LangContext)
    const [ unitPrice, setUnitPrice ] = useState(item.basePrice)
    const [ numItems, setNumItems ] = useState(1)
    const options = new item().getOptions();

    const handleOnChange = (event) => {
        setNumItems(event.target.value);
    }

    return (
        <div className="flex flex-col items-start w-1/3 border-[1px] min-w-[400px] max-w-[500px] rounded-sm border-solid border-black m-5">
            <div className="flex flex-row w-full justify-between items-center p-4">
            <div className="flex flex-col items-start">
                <h1 className="text-3xl font-black mb-2">{translation[lang][item.name]}</h1>
                <h1 className="mb-1 mt-2 text-lg">${item.basePrice}</h1>
            </div>
            <img src={require(`./img/${item.name}.jpeg`)} className="w-24 h-24 object-cover rounded-sm"/>
            </div>
            
            <hr className="border-black border-t-[1px] rounded-sm w-full" />
            <div className="p-3 flex flex-col items-start w-full">
                {
                    options.map(option => <div className="mb-2 pb-3 border-b-[1px] border-black w-full"><Option item={item} option={option} uniPrice={unitPrice} setUnitPrice={setUnitPrice}/></div>)
                }
            </div>
            <div className="flex flex-row justify-between items-center w-full py-3 px-5 mt-[-20px]">
                <input className="text-sm text-white  bg-gray-900 pl-6 p-[2.5px] rounded-sm" onChange={handleOnChange} type="number" defaultValue={1} min={1} max={5}/>
                <button className="text-sm text-white bg-gray-900 px-3 py-1 rounded-sm">Add ${unitPrice * numItems}</button>
            </div>
        </div>
    )
}

export default ItemOrder