<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Playground</title>
    <script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/brython/3.10.0/brython.min.js"></script>
</head>
<body>
    <header>
        <h1>Python Playground</h1>
    </header>
    <main>
        <section>
            <h2>Python Execution</h2>
            <textarea id="code" rows="5" cols="50">print("Hello World")</textarea><br>
            <button id="run">Run Code</button>
            <h3>Output</h3>
            <pre id="output"></pre>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 Python Playground</p>
    </footer>
    <script>
        document.getElementById('run').addEventListener('click', function() {
            var code = document.getElementById('code').value;
            var output = document.getElementById('output');
            
            try {
                var stdout = '';
                var stderr = '';
                function brython_stdout(data) {
                    stdout += data;
                }
                function brython_stderr(data) {
                    stderr += data;
                }
                
                document.body.innerHTML += '<script type="text/python">' + code + '</script>';
                brython_run_script();
                
                output.textContent = stdout + stderr;
            } catch (error) {
                output.textContent = 'Error: ' + error.message;
            }
        });
    </script>
</body>
</html>
