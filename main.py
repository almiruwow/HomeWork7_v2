from functions import get_student_by_pk, get_profession_by_title, check_fitness


def main():
    while True:
        user_input = input('Введите номер студента\n')

        student = get_student_by_pk(int(user_input))

        if student is None:
            print('У нас нет такого студента')
            quit()
        else:
            print(f'Студент: {student["full_name"]}\n'
                  f'Знает {" ".join(student["skills"])}\n')

        user_input = input(f'Выберите специальность для оценки студента {student["full_name"]}\n')

        profession = get_profession_by_title(user_input.title())

        if profession is None:
            print('У нас нет такой специальности')
            quit()
        else:
            data = check_fitness(student, profession)
            print(f'Пригодность {data["fit_percent"]}%\n'
                  f'{student["full_name"]} знает {" ".join(data["has"])}\n'
                  f'{student["full_name"]} не знает {" ".join(data["lacks"])}\n')


if __name__ == '__main__':
    main()