if __name__ == '__main__':
    no_Eyfa_image, _ = list(map(int, input().split()))

    predict_ehfeha = []

    for idx in range(no_Eyfa_image):
        current_Eyfa = input()

        predict_ehfeha.append("")

        for c in current_Eyfa:
            predict_ehfeha[idx] += c
            predict_ehfeha[idx] += c

    Eyfa_flag = True

    for idx in range(no_Eyfa_image):
        current_ehfeha = input()
        if current_ehfeha != predict_ehfeha[idx]:
            Eyfa_flag = False
            break

    print("{}Eyfa".format("Not " if Eyfa_flag is False else ""))
