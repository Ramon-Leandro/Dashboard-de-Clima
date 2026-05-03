import { useState, useEffect } from 'react' // As "ferramentas especiais" do React
import './App.css'

function App() {
  // --- 1. ESTADOS (A Memória do Componente) ---
  const [cidade, setCidade] = useState('')        // Guarda o texto que o usuário digita no input
  const [clima, setClima] = useState(null)        // Guarda os dados do clima que recebemos do backend  
  const [historico, setHistorico] = useState([])  // Guarda a lista de buscas vinda do Banco de Dados


  // --- 2. FUNÇÃO PARA BUSCAR CLIMA ---
  const buscarClima = async () => {
    if (!cidade) return alert("Digite o nome de uma cidade!") // Evita buscas vazias
    
    try {
      // Faz o "pedido" para a rota que criamos no Flask
      const response = await fetch(`http://127.0.0.1:5000/clima?cidade=${cidade}`)
      const data = await response.json() // Transforma a resposta em um objeto JS
      
      if (data.erro) {
        alert(data.erro)
      } else {
        setClima(data)
        buscarHistorico() // Atualiza o histórico sempre que busca um novo
      }
    } catch (error) {
      console.error("Erro ao buscar clima:", error)
    }
  }

  // --- 3. FUNÇÃO PARA BUSCAR O HISTÓRICO ---
  const buscarHistorico = async () => {
    try {
      // Faz o pedido para a rota /historico do Python
      const response = await fetch('http://127.0.0.1:5000/historico')
      const data = await response.json()
      setHistorico(data) // Atualiza a lista do histórico com os dados do SQLite
    } catch (error) {
      console.error("Erro ao buscar histórico:", error)
    }
  }

  // Carregar o histórico assim que abrir a página
  // Esse hook executa o código assim que a página termina de carregar.
  // Usamos isso para que o histórico já apareça na tela sem o usuário precisar clicar em nada.
  useEffect(() => {
    buscarHistorico()
  }, [])

  // --- 6. O DESENHO DA PÁGINA (HTML/JSX) ---
  return (
    <div className="App">
      <h1>🌤️ Dashboard de Clima</h1>
      
      {/* SEÇÃO DE BUSCA */}
      <div className="busca">
        <input 
          type="text" 
          placeholder="Digite a cidade..." 
          value={cidade}
          onChange={(e) => setCidade(e.target.value)}
        />
        <button onClick={buscarClima}>Buscar</button>
      </div>
      {/* EXIBIÇÃO DO CLIMA ATUAL (Só aparece se 'clima' não for nulo) */}
      {clima && (
        <div className="card-clima">
          <h2>{clima.cidade}</h2>
          <p className="temp">{clima.temperatura}°C</p>
          <p>{clima.descricao}</p>
        </div>
      )}

      <hr />

      {/* TABELA DE HISTÓRICO */}
      <h3>📜 Histórico de Consultas</h3>
      <table border="1" style={{ width: '100%', marginTop: '20px' }}>
        <thead>
          <tr>
            <th>Cidade</th>
            <th>Temp.</th>
            <th>Descrição</th>
            <th>Data</th>
          </tr>
        </thead>
        <tbody>
          {/* O .map percorre a lista 'historico' e cria uma linha <tr> para cada item */}
          {historico.map((item) => (
            <tr key={item.id}>
              <td>{item.cidade}</td>
              <td>{item.temperatura}°C</td>
              <td>{item.descricao}</td>
              <td>{item.data}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default App