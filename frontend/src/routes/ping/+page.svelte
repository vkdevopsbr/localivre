<script>
    import { fetchData } from '$lib/api.js';
    let message = ''; // Inicialmente vazio

    async function loadPing() {
        message = await fetchData('localivre-ping'); // Chama a função e define a mensagem
    }
</script>

<main>
    <h1>Testar Ping</h1>
    <button on:click={loadPing}>Testar Ping Endpoint</button>

    <p>{message}</p> <!-- Exibe a mensagem retornada -->
</main>

<style>
    button {
        padding: 10px 20px;
        background-color: #007BFF;
        color: white;
        border: none;
        cursor: pointer;
    }
    button:hover {
        background-color: #0056b3;
    }
</style>
