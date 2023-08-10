def calculate_imc(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def interpret_imc(bmi):
    categories = [
        ("Abaixo do Peso", bmi < 18.5),
        ("Peso Normal", 18.5 <= bmi < 25),
        ("Sobrepeso", 25 <= bmi < 30),
        ("Obesidade Classe I", 30 <= bmi < 35),
        ("Obesidade Classe II", 35 <= bmi < 40),
        ("Obesidade Classe III", bmi >= 40)
    ]

    for category, condition in categories:
        if condition:
            return category

weight = float(input("Digite o seu peso em kg: "))
height = float(input("Digite a sua altura em metros: "))

imc = calculate_imc(weight, height)
imc_category = interpret_imc(imc)

print(f"Seu IMC é {imc:.2f} e você está na categoria: {imc_category}")
