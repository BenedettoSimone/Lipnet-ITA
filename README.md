# LipReadingITA

Keras implementation of the method described in the paper 'LipNet: End-to-End Sentence-level Lipreading' by Yannis M. Assael, Brendan Shillingford, Shimon Whiteson, and Nando de Freitas (https://arxiv.org/abs/1611.01599).
Reference - https://github.com/rizkiarm/LipNet


## Requirements
```
---------
```









## Dataset
In this project we will use an Italian dataset containing the following sentences.


|        Task       |   ID   |        Task       |   ID   |
|:-----------------:|:------:|:-----------------:|:------:|
|  Salve quanto costa quell' articolo?  |   0   |  Tutto bene, grazie.  |   10   |
|  È in offerta, costa 10 euro.  |   1   |  Prendiamo un caffè al bar?  |   11   |
|  Perfetto, vorrei comprarne due.  |   2   |  Certo volentieri, io lo prenderò macchiato.  |   12   |
|  Certo ecco a lei, vuole un sacchetto?  |   3   |  A che ora arriva il pullman?  |   13   |
|  Sì, grazie e arrivederci.  |   4   |  Dovrebbe arrivare tra qualche minuto.  |   14   |
|  Le auguro una buona giornata.  |   5   |  Quanto costa il biglietto?  |   15   |
|  Buongiorno, io sono Mario.  |   6   |  Purtroppo non lo so, però potresti chiedere all’autista.  |   16   |
|  Buonasera, io sono Mario.  |   7   |  Va bene, grazie lo stesso.  |   17   |
|  Piacere Luigi, come stai?  |   8   |  Prego.  |   18   |
|  Tutto bene, tu?  |  9   |


<br><br>
For the dataset building, we created a tool to record the videos (https://github.com/BenedettoSimone/Video-Recorder). The videos have a dimension of ``360x288 x 25fps``. Use the information provided in the repository and on the main page to replicate our work.
<br><br>After gathering the videos for each subject, we organized the dataset with the following structure.

```
Dataset:
├───s1
│   ├───0-bs.mpg
│   ├───1-bs.mpg
│   └───...
├───s2
│   └───...
└───...
    └───...
```

