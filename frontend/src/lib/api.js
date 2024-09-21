export async function fetchData(endpoint) {
    try {
        const response = await fetch(`${import.meta.env.VITE_API_URL}/${endpoint}`);
        if (!response.ok) {
            throw new Error('Erro ao conectar ao servidor');
        }
        const data = await response.json();
        return data.message;
    } catch (error) {
        console.error('Erro:', error);
        return 'Erro ao buscar dados';
    }
}
