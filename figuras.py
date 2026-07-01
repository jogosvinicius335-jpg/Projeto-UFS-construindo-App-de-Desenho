from abc import ABC, abstractmethod

class Figura(ABC):
    def __init__(self, x1, y1, x2, y2, cor_borda):
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.cor_borda = cor_borda

    def atualizar(self, x, y):
        self.x2, self.y2 = x, y

    @abstractmethod
    def desenhar(self, canvas, tracejado=False):
        pass

    def esta_incompleta(self):
        return (self.x1, self.y1) == (self.x2, self.y2)

    def _opcoes_desenho(self, tracejado=False):
        # Coloque aqui Danilo sua parte
        pass


class FiguraPreenchida(Figura):
    def __init__(self, x1, y1, x2, y2, cor_borda, cor_preenchimento):
        # Coloque aqui Danilo sua parte
        pass

    def _opcoes_desenho(self, tracejado=False):
        # Coloque aqui Danilo sua parte
        pass


class Linha(Figura):
    def desenhar(self, canvas, tracejado=False):
        # Coloque aqui Danilo sua parte
        pass


class Rabisco(Figura):
    def __init__(self, x, y, cor_borda):
        # Coloque aqui Danilo sua parte
        pass

    def atualizar(self, x, y):
        # Coloque aqui Danilo sua parte
        pass

    def esta_incompleta(self):
        # Coloque aqui Danilo sua parte
        pass

    def desenhar(self, canvas, tracejado=False):
        # Coloque aqui Danilo sua parte
        pass


class Retangulo(FiguraPreenchida):
    def desenhar(self, canvas, tracejado=False):
        canvas.create_rectangle(
            self.x1, self.y1, self.x2, self.y2,
            **self._opcoes_desenho(tracejado)
        )


class Oval(FiguraPreenchida):
    def desenhar(self, canvas, tracejado=False):
        canvas.create_oval(
            self.x1, self.y1, self.x2, self.y2,
            **self._opcoes_desenho(tracejado)
        )

