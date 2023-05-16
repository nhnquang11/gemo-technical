import { useState, createContext } from "react";

const LangContext = createContext()

function LangProvider({ children }) {
    const [lang, setLang] = useState('en')

    const toggleLang = () => {
        setLang(lang === 'en' ? 'vn' : 'en')
    }

    const context = {
        lang,
        toggleLang
    }

    return (
        <LangContext.Provider value={context}>
            {children}
        </LangContext.Provider>
    )
}

export { LangContext, LangProvider }