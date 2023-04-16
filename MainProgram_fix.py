from SingleLinkedList import SingleLinkedList
from random import randint

class Game():
    def __init__(self):
        self.LL_player = SingleLinkedList() #player status
        self.LL_platform = SingleLinkedList() #siapa yang bisa rusak apa ga, random platform status
        self.LL_finish = SingleLinkedList() #jika 0 belum finish / mati; kalau 1 berarti finish
        self.LLplatform_traveled = SingleLinkedList() #0 artinya di udah diinjak dan rusak, 1 artinya bisa belum diinjak atau sudah diinjak & tidak bisa rusak
        self.LLcordinate_player = SingleLinkedList()
    
    def startGame(self):
        player = int(input("Masukkan Jumlah Player : "))
        platform = (player + 1) * 2

        #isi player status dan finish
        for i in range(0, player):
            self.LL_player.add(1)
            self.LL_finish.add(0)
        
        #random platform
        random = None
        for i in range(0, platform):
            if(i % 2 == 0):
                random = randint(0, 1)
                self.LL_platform.add(random)
            
            if(i % 2 == 1 and random == 1):
                self.LL_platform.add(0)
            elif(i % 2 == 1 and random == 0):
                self.LL_platform.add(1)

        # isi platform travelled
        for i in range(0, platform):
            self.LLplatform_traveled.add(1)

        # isi LL cordinate player
        # kalo data = -1 artinya dia di start
        # kalo data = -2 artinya dia di finish
        # kalo data = -3 artinya dia mati
        for i in range(0, player):
            self.LLcordinate_player.add(-1)

        # buat bantu, bisa dihapus
        # print("Cheat")
        # self.LL_platform.printList()

    def printPlatform(self, i):
        for k in range(0, main_game.LL_player.size):
            if(main_game.LLcordinate_player.getData(k) == -1):
                print(k + 1, end=" ")

                if (k + 1) % 3 == 0:
                    print("\n")
                        
        if main_game.LL_player.size < 3:
            print("\n")

        print("\n START")
        print("-------")
        for j in range(0, int(self.LL_platform.size / 2)):
            print("=== ===\n|", end="") #template 1

            if(self.LLplatform_traveled.getData(j * 2) == '0'):
                print("X", end="")
            elif(self.LL_platform.getData(i - 1) < 0):
                print(" ", end="")
            elif(j * 2 == self.LLcordinate_player.getData(i - 1) or (j * 2) + 1 == self.LLcordinate_player.getData(i-1)):
                if(self.LLcordinate_player.getData(i - 1) % 2 == 0):
                    print(i, end="")
                else:
                    print(" ", end="")
            else:
                print(" ", end="")
            
            print("| |", end="") #template 2
            
            if(self.LLplatform_traveled.getData((j * 2)+1) == '0'):
                print("X", end="")
            elif(self.LL_platform.getData(i - 1) < 0):
                print(" ", end="")
            elif(j * 2 == self.LLcordinate_player.getData(i-1) or (j * 2) + 1 == self.LLcordinate_player.getData(i-1)):
                if(self.LLcordinate_player.getData(i-1) % 2 == 1):
                    print(i, end="")
                else:
                    print(" ", end="")
            else:
                print(" ", end="")
            
            print("|\n=== ===\n", end="") #template 3
        print("-------")
        print("  END")

        for k in range(0, main_game.LL_player.size):
            if(int(main_game.LLcordinate_player.getData(k)) == -2):
                print(k + 1, end=" ")

                if (k + 1) % 3 == 0:
                    print("\n")
                        
        if main_game.LL_player.size < 3:
            print("\n")

        print("\n=======\n")
    
    def printStatus(self, data, i):
        # 1 artinya sedang bermain
        # 2 artinya memilih platform yang salah
        # 3 artinya telah mati
        # 4 artinya memilih platform yang benar
        # 5 artinya sampai ke finish

        string1 = "Player " + str(i)

        if data == 1: # sedang bermain
            string1 = string1 + " sedang bermain!"
            value = len(string1)

            template1 = "#" + ("-" * value) + "#"
            result = template1 + "\n|" + string1 + "|\n" + template1 + "\n"
            print(result)
        elif data == 2: #platform salah
            string1 = string1 + " memilih platform yang salah!"
            value = len(string1)

            template1 = "x" + ("-" * value) + "x"
            result = template1 + "\n|" + string1 + "|\n" + template1 + "\n"
            print(result)
        elif data == 3: #telah mati
            string1 = string1 + " telah mati"
            value = len(string1)

            template1 = "x" + ("-" * value) + "x"
            result = template1 + "\n|" + string1 + "|\n" + template1 + "\n"
            print(result)
        elif data == 4: #platform benar
            string1 = string1 + " memilih platform yang benar!"
            value = len(string1)

            template1 = "*" + ("-" * value) + "*"
            result = template1 + "\n|" + string1 + "|\n" + template1 + "\n"
            print(result)
        elif data == 5: #finish
            string1 = string1 + " sampai ke finish!"
            value = len(string1)

            template1 = "$" + ("-" * value) + "$"
            result = template1 + "\n|" + string1 + "|\n" + template1 + "\n"
            print(result)

        
# Main
main_game = Game()

main_game.startGame()

for i in range(1, main_game.LL_player.size + 1): #jadi semua player akan dimainkan
    main_game.printStatus(1, i)

    finish = False #finish nya ini untuk 1 player, jadi akan diupdate untuk setiap player
    step = 0 #track langkah player sekarang

    while finish is not True:
        index2 = 0 #variabel global untuk platform travelled

        if step == 0:
            main_game.printPlatform(i)

        print("\nPilih gerakan yang ingin dilakukan")
        print("1. Player", i, "memilih platform kiri")
        print("2. Player", i, "memilih platform kanan")
        pilihan1 = int(input("Input : "))

        # cek permainan
        if pilihan1 == 1: #milih kiri
            index = (2 * step)

            if int(main_game.LL_platform.getData(index)) == 0:
                main_game.printStatus(2, i)
                main_game.printStatus(3, i)

                # index nya i-1 karena loop nya aku mulai dari 1
                index_update = i - 1
                main_game.LL_player.update('0', index_update) #player i tidak ada di start
                main_game.LL_finish.update('0', index_update) #player i tidak ada di finish (artinya dia mati)

                # update kordinat player i
                player_number = i - 1
                main_game.LLcordinate_player.update('-3', player_number) #karena dia mati makanya di isi 0
                
                # update LL platform traveled nya 
                main_game.LLplatform_traveled.update('0', index)

                # jika mati tidak perlu print platform karena, nanti akan di print di line 162

                finish = True #lanjut ke player 2
                break
            elif int(main_game.LL_platform.getData(index)) == 1:
                main_game.printStatus(4, i)

                step = step + 1

                # update kordinat player i
                player_number = i - 1
                main_game.LLcordinate_player.update(index, player_number) 

                main_game.printPlatform(i)

            # cek finish
            cek = step * 2
            size = main_game.LL_platform.getSize()
            if cek == size:
                main_game.printStatus(5, i)
                index_update = i - 1
                main_game.LL_player.update('0', index_update) #player i sudah tidak ada di start
                main_game.LL_finish.update('1', index_update) #tapi player i ada di finish

                # update kordinat player i
                player_number = i - 1
                main_game.LLcordinate_player.update('-2', player_number) 
                main_game.printPlatform(i)

                finish = True

                break
            #game masih berlanjut
        elif pilihan1 == 2:
            index = (2 * step) + 1

            if int(main_game.LL_platform.getData(index)) == 0: #kalau pilih yg rusak
                main_game.printStatus(2, i)
                main_game.printStatus(3, i)

                # index nya i-1 karena loop nya aku mulai dari 1
                index_update = i - 1
                main_game.LL_player.update('0', index_update) #player i tidak ada di start
                main_game.LL_finish.update('0', index_update) #player i tidak ada di finish (artinya dia mati)

                # update LL platform traveled nya
                main_game.LLplatform_traveled.update('0', index)
                index2 = index2 + 1
                main_game.LLplatform_traveled.update('1', index2)

                # update kordinat player i
                player_number = i - 1
                main_game.LLcordinate_player.update('-3', player_number) #karena dia mati makanya di isi 0

                # update LL platform traveled nya
                main_game.LLplatform_traveled.update('0', index)

                # jika mati tidak perlu print platform karena, nanti akan di print di line 162
            
                finish = True #lanjut ke player 2

                break

            elif int(main_game.LL_platform.getData(index)) == 1:
                main_game.printStatus(4, i)

                step = step + 1

                # update kordinat player i
                player_number = i - 1
                main_game.LLcordinate_player.update(index, player_number) 

                main_game.printPlatform(i)
            
            # cek finish
            cek = step * 2
            size = main_game.LL_platform.getSize()
            if cek == size:
                main_game.printStatus(5, i)

                index_update = i - 1
                main_game.LL_player.update('0', index_update) #player i sudah tidak ada di start
                main_game.LL_finish.update('1', index_update) #tapi player i ada di finish

                # update kordinat player i
                player_number = i - 1
                main_game.LLcordinate_player.update('-2', player_number) 

                finish = True
                break
        
winner = [] 
loser = []
for i in range(0, main_game.LL_finish.getSize()):

    nomor = i + 1
    player = "Player" + str(nomor)

    if main_game.LL_finish.getData(i) == '1':
        winner.append(player) 
    elif main_game.LL_finish.getData(i) == '0':
        loser.append(player)

# print winner
if(len(winner) > 0):
    print("!!!WINNER!!!")
    value = len(winner[len(winner) - 1])
    template1 = "#" + ("-" * value) + "#"

    result = template1 + "\n"
    for i in range(0, len(winner)):
        string1 = "|" + winner[i] + "|\n"
        result += string1
        
    result += template1 + "\n"
    print(result)

# print loser
if(len(loser) > 0):
    print("!!!LOSER!!!")
    value = len(loser[len(loser) - 1])
    template1 = "#" + ("-" * value) + "#"

    result = template1 + "\n"
    for i in range(0, len(loser)):
        string1 = "|" + loser[i] + "|\n"
        result += string1
        
    result += template1 + "\n"
    print(result)

# print game selesai
string1 = ""
string1 = string1 + "Game Selesai!"
value = len(string1)

template1 = "^" + ("-" * value) + "^"
result = template1 + "\n|" + string1 + "|\n" + template1 + "\n"
print(result)