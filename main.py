from fastapi import FastAPI

app=FastAPI()


aluno_info = {
    "nome": "Thauany",
    "email": "thauanyh12@gmail.com",
    "curso": "Sistemas de Informação",
    "github": "https://github.com/HonoratoThauany",
    "cidade": "Juazeiro do Norte",
}

@app.get("/health")
def health_check():
    """
    Verifica se a aplicação está funcionando.
    """
    return {"status": "ok"}

@app.get("/me")
def get_thauany_info():
    """
    Retorna informações sobre o aluno.
    """
    return aluno_info
