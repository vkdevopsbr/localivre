<script>
    let message = "Bem-vindo ao Localivre!";
</script>

<main>
    <h1>{message}</h1>
    <p>Esta é a página inicial do Localivre.</p>

    <nav>
        <a href="/ping">Testar Ping</a>
        <a href="/db_test">Testar Conexão ao Banco</a>
    </nav>
</main>

<style>
    nav {
        margin-top: 20px;
    }
    nav a {
        margin-right: 10px;
        text-decoration: none;
        color: blue;
    }
    nav a:hover {
        text-decoration: underline;
    }
</style>
