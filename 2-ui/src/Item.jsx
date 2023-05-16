import translation from "./translation"
import { useContext, useState } from 'react';
import { LangContext } from './LangContext';
import ItemOrder from "./ItemOrder";


function Item({item}) {
    const { lang } = useContext(LangContext)
    const [showOrder, setShowOrder] = useState(false);

    const handleOnClick = () => {
        setShowOrder(true);
    }

    const handleExitOnClick = () => {
        setShowOrder(false);
    }

    return (
        <div>
            <button onClick={handleOnClick} className="flex flex-col items-start w-1/3 border-[1px] min-w-[400px] max-w-[500px] rounded-sm border-solid border-black m-3">
                <div className="flex flex-row w-full justify-between items-center p-4">
                    <div className="flex flex-col items-start">
                        <h1 className="text-3xl font-black mb-2">{translation[lang][item.name]}</h1>
                        <h1 className="mb-1 mt-2 text-lg">${item.basePrice}</h1>
                    </div>
                    <img src={require(`./img/${item.name}.jpeg`)} className="w-24 h-24 object-cover rounded-sm"/>
                </div>
            </button>
            { showOrder && 
                <div className="fixed top-0 bottom-0 right-0 left-0 bg-white flex items-center justify-center">
                    <div><ItemOrder item={item} /></div>
                    <button onClick={handleExitOnClick} className="fixed right-2 top-2">X</button>
                </div>
            }
        </div>
    )
}

export default Item