
# source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ",]
def read_csv():
  import csv
  with open('source.csv','r')as f:
      reader = f.read()
      return reader
    

def search():
    word = input("鬼滅の登場人物の名前を入力してください>>")
    kime = read_csv()
    if word in kime:
          print(f"{word}が見つかりました")
    else:
          print(f"{word}が見つかりませんでした")
          # source.append(word)
          with open('source.csv','a') as f:
            
            f.write('\n'+ word)
if __name__ == "__main__":
  search()
