import tkinter as tk
import paramiko

def apagar_remotamente():
    ip_remota = ip_entry.get()
    usuario_remoto = usuario_entry.get()
    contraseña_remota = contraseña_entry.get()
    
    try:
        # Establecer la conexión SSH
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh_client.connect(ip_remota, username=usuario_remoto, password=contraseña_remota)

        # Enviar el comando de apagado
        stdin, stdout, stderr = ssh_client.exec_command("sudo shutdown -h now")

        # Esperar a que el comando termine
        stdout.channel.recv_exit_status()

        resultado_label.config(text="La computadora se ha apagado correctamente.", fg="green")
    except paramiko.AuthenticationException:
        resultado_label.config(text="Error de autenticación. Verifica las credenciales proporcionadas.", fg="red")
    except paramiko.SSHException as e:
        resultado_label.config(text="Error al establecer la conexión SSH: " + str(e), fg="red")
    finally:
        ssh_client.close()

# Crear la ventana
ventana = tk.Tk()
ventana.title("Apagar computadora remota")

# Crear etiquetas y campos de entrada
tk.Label(ventana, text="IP remota:").grid(row=0, column=0, padx=5, pady=5)
ip_entry = tk.Entry(ventana)
ip_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(ventana, text="Usuario remoto:").grid(row=1, column=0, padx=5, pady=5)
usuario_entry = tk.Entry(ventana)
usuario_entry.grid(row=1, column=1, padx=5, pady=5)

tk.Label(ventana, text="Contraseña remota:").grid(row=2, column=0, padx=5, pady=5)
contraseña_entry = tk.Entry(ventana, show="*")
contraseña_entry.grid(row=2, column=1, padx=5, pady=5)

# Botón para apagar la computadora remota
apagar_button = tk.Button(ventana, text="Apagar", command=apagar_remotamente, bg="red")
apagar_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

# Etiqueta para mostrar el resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

# Ejecutar la aplicación
ventana.mainloop()


