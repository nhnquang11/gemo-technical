import './App.css';
import MENU from './menu';
import { useContext } from 'react';
import { LangContext } from './LangContext';
import ItemOrder from './ItemOrder';
import Item from './Item';

function App() {
  const { lang, toggleLang } = useContext(LangContext)

  return (
    <div className="App flex flex-col justify-center items-center pb-5">
      <button className='font-mono border-black border-[1px] px-1 rounded-sm mt-5' onClick={toggleLang}>{lang}</button>
      {
        MENU.map(item => <Item item={item} />)
      }
    </div>
  );
}

export default App;
