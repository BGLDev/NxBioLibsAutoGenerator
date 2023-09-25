import subprocess

from Models.base_config import BaseConfig


class ExecuteNxFormatWrite:
    def __init__(self, config: BaseConfig):
        # self.proyect_origin_path = f"{config.proyect_origin_path}"
        self.proyect_origin_path = f"/home/benat/Personal/01 - BIOLAN Proyects/01 - Biolan global/biolan"
        self.command = f"npx nx format:write"
        try:
            result = subprocess.run(self.command, cwd=self.proyect_origin_path, shell=True, check=True, stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            # El argumento "cwd" establece el directorio de trabajo actual para la ejecución del comando.
            # El argumento "shell=True" permite usar una cadena de comando en lugar de una lista de argumentos.
            # El argumento "check=True" generará una excepción si el comando falla.
            # Los argumentos "stdout=subprocess.PIPE" y "stderr=subprocess.PIPE" capturan la salida estándar y de error.

            # Imprime la salida estándar y de error
            print("Salida estándar:", result.stdout.decode())
            print("Salida de error:", result.stderr.decode())

        except subprocess.CalledProcessError as e:
            # Captura excepciones si el comando falla
            print("El comando falló con el código de salida:", e.returncode)
            print("Salida de error:", e.stderr.decode())


proyect_origin_path = f"/home/benat/Personal/01 - BIOLAN Proyects/01 - Biolan global/biolan"
command = f"npx nx format:write"
try:
    result = subprocess.run(command, cwd=proyect_origin_path, shell=True, check=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    # El argumento "cwd" establece el directorio de trabajo actual para la ejecución del comando.
    # El argumento "shell=True" permite usar una cadena de comando en lugar de una lista de argumentos.
    # El argumento "check=True" generará una excepción si el comando falla.
    # Los argumentos "stdout=subprocess.PIPE" y "stderr=subprocess.PIPE" capturan la salida estándar y de error.

    # Imprime la salida estándar y de error
    print("Salida estándar:", result.stdout.decode())
    print("Salida de error:", result.stderr.decode())

except subprocess.CalledProcessError as e:
    # Captura excepciones si el comando falla
    print("El comando falló con el código de salida:", e.returncode)
    print("Salida de error:", e.stderr.decode())