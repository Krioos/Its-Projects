const elementRoot = document.getElementById("root");
const root = ReactDOM.createRoot(elementRoot);

const App=()=>{
    return(
        <main className="main">
            <h1>Primo componente App</h1>
        </main>
    )
}

const List=()=>{
    return(
        <ul>
            <li>PHP</li>
            <li>JS</li>
            <li>Python</li>
        </ul>
    )
}

root.render(
    <>
    <App></App>
    <List></List>
    </>
)

