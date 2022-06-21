import os

phrases = ['Salve quanto costa quell\' articolo',
           'E\' in offerta, costa 10 euro',
           'Perfetto vorrei comprarne due.',
           'Certo ecco a lei vuole un sacchetto',
           'Si\' grazie e arrivederci',
           'Le auguro una buona giornata',
           'Buongiorno io sono Mario',
           'Buonasera io sono Mario',
           'Piacere Luigi come stai',
           'Tutto bene tu',
           'Tutto bene grazie',
           'Prendiamo un caffe\' al bar',
           'Certo volentieri, io lo prendero\' macchiato',
           'A che ora arriva il pullman',
           'Dovrebbe arrivare tra qualche minuto',
           'Quanto costa il biglietto',
           'Purtroppo non lo so pero\' potresti chiedere all\' autista',
           'Va bene grazie lo stesso',
           'Prego'
           ]


def write_file(file, index):
    if file is not None:
        splitted_phrases = phrases[int(index)].split()
        file.write("sil\n")
        for word in splitted_phrases:
            file.write(word + "\n")
        file.write("sil")


if __name__ == '__main__':
    main_path = input("Enter dataset path:")
    main_path=main_path+"/"
    os.chdir(main_path)
    print(os.getcwd())
    for dir in os.listdir():
        # dir s*
        os.chdir(dir)

        for video in os.listdir():
            if ".txt" not in video:
                print(video)
                index = ""
                dash = video.rfind("-")

                index = video[0:(dash)]
                print(index)
                with open(video[:-4] + ".txt", 'w+') as file_name:
                    write_file(file_name, index)

        os.chdir("..")
    os.chdir("..")
