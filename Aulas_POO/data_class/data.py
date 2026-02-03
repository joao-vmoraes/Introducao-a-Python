from dataclasses import dataclass, field

@dataclass
class Pessoa:
    nome: str = field(
        default="joao"
        )
    idade: int = field(
        default=21
    )
    enderecos: list[str] = field(default_factory=list)

p1 = Pessoa('Paulko', 223)
print(p1)
