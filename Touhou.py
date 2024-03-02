def touhou_dicipline_generator (n: int) -> str:
    result ='東方'
    for i in range(n):
        result +='廚自重'
    return result

if __name__ == "__main__":
        print(touhou_dicipline_generator(int(input("how many times: "))))