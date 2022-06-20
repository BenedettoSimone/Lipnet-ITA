# LipReadingITA

Keras implementation of the method described in the paper 'LipNet: End-to-End Sentence-level Lipreading' by Yannis M. Assael, Brendan Shillingford, Shimon Whiteson, and Nando de Freitas (https://arxiv.org/abs/1611.01599).
Reference - https://github.com/rizkiarm/LipNet


## 1. Requirements
```
---------
```









## 2. Dataset
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

<br>

### 2.1 Building
For the dataset building, we created a tool to record the videos (https://github.com/BenedettoSimone/Video-Recorder). The videos have a dimension of ``360x288 x 25fps``. Use the information provided in the repository and on the main page to replicate our work.
<br><br>After gathering the videos for each subject, we organized the dataset with the following structure.

```
Dataset:
├───s1
│   ├─── 0-bs.mpg
│   ├─── 1-bs.mpg
│   └───...
├───s2
│   └───...
└───...
    └───...
```

### 2.2 Forced alignment
Then, we applied for each video the audio and text synchronization (aka forced alignment) using [Aeneas](https://github.com/readbeyond/aeneas). The output of each file follows this format:
<details><summary>Show format</summary>
<p>

```ruby
{
 "fragments": [
  {
   "begin": "0.000",
   "children": [],
   "end": "0.480",
   "id": "f000001",
   "language": "eng",
   "lines": [
    "sil"
   ]
  },
  {
   "begin": "0.480",
   "children": [],
   "end": "0.760",
   "id": "f000002",
   "language": "eng",
   "lines": [
    "Bin"
   ]
  },
  {
   "begin": "0.760",
   "children": [],
   "end": "1.160",
   "id": "f000003",
   "language": "eng",
   "lines": [
    "Blue"
   ]
  },
  {
   "begin": "1.160",
   "children": [],
   "end": "1.360",
   "id": "f000004",
   "language": "eng",
   "lines": [
    "at"
   ]
  },
  {
   "begin": "1.360",
   "children": [],
   "end": "1.600",
   "id": "f000005",
   "language": "eng",
   "lines": [
    "d"
   ]
  },
  {
   "begin": "1.600",
   "children": [],
   "end": "1.960",
   "id": "f000006",
   "language": "eng",
   "lines": [
    "Seven"
   ]
  },
  {
   "begin": "1.960",
   "children": [],
   "end": "2.360",
   "id": "f000007",
   "language": "eng",
   "lines": [
    "soon"
   ]
  },
  {
   "begin": "2.360",
   "children": [],
   "end": "2.960",
   "id": "f000008",
   "language": "eng",
   "lines": [
    "sil"
   ]
  }
 ]
}
```
</p>
</details>

As a final step, we transformed each json file into an ``.align`` file having the following format:
```
0 12000 sil
12000 19000 Bin
19000 28999 Blue
28999 34000 at
34000 40000 d
40000 49000 Seven
49000 59000 soon
59000 74000 sil
```
The first number indicates the start of that word. The second number indicates the stop. Each number represent the frame numbers x 1000. So frames 0-12 are silence, frames 12-19 are the word "bin", etc. To perform this conversion ....


## Developed by
[Simone Benedetto](https://github.com/BenedettoSimone) <br>
[Salerno Daniele](https://github.com/DanieleSalerno)
