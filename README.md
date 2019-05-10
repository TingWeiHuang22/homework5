# homework5
  
**電腦視覺特效-第六組**  
  
##  Multi-view images
此部分吾組拍攝Multi-view images的主軸是以以鴨子為中心點進行拍攝。並且於拍攝完一張圖片後向右平移一小段並繼續拍攝下一張圖片!<br><br>
<第一張圖><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/1.jpg" width="300" height="300"><br>
<第二張圖><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/2.jpg" width="300" height="300"><br>
<第三張圖><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/3.jpg" width="300" height="300"><br>
<第四張圖><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/4.jpg" width="300" height="300">

##  Image alignment results
此部分吾組利用ORB這個feature extrators來對兩張不同的圖片產生matching以及alignment後的結果。而圖片的來源則是從第一部分的4張圖片而來!<br><br>

<第一張圖片與第二張圖片matching的結果/第一張圖片與第二張圖片alignment後的結果><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/12/matches_ORB.jpg" width="500" height="250">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/12/align_ORB.jpg" width="250" height="250"><br>
<第一張圖片與第三張圖片matching的結果/第一張圖片與第三張圖片alignment後的結果><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/13/matches_ORB.jpg" width="500" height="250">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/13/align_ORB.jpg" width="250" height="250"><br>
<第一張圖片與第四張圖片matching的結果/第一張圖片與第四張圖片alignment後的結果><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/14/matches_ORB.jpg" width="500" height="250">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/14/align_ORB.jpg" width="250" height="250"><br>

由上圖3張matching的結果，可以看出我們兩張不同的圖片feature最相近的部分皆有坐落下鴨子的身體部份上(吾組有調整程式的參數好讓matching的線皆坐落於鴨子身上，而這用意在於避免alignment後的圖片會有過度變形失真抑或是偏移的情況)。然而從三張alignment的結果可以看出，第一、二張aligment的圖片呈現的結果比起第一、三張以及第一、四張的結果還要好(即alignment後的圖片黑色部分較少)，吾組推測這其中的在於位移量的影響。為何吾組會這樣說呢，因為第一、二張圖片的拍攝的位移量比起其他第一、三張圖片以及第一、四張圖片的位移量來說是最小的，而其他拍攝物大致上皆沒有改變，所以吾組才會如此推測。                                                                                                                      

## Multi-view 3D visual effects
此部份吾組要實作的3D visual effects為Motion parallax<br><br>

<第一張圖片與第一、二張align後的圖片所產生的gif><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/12/12.gif" width="500" height="500"><br>
<第一張圖片與第一、三張align後的圖片所產生的gif><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/13/13.gif" width="500" height="500"><br>
<第一張圖片與第一、四張align後的圖片所產生的gif><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/14/14.gif" width="500" height="500">

由上面三組gif的結果比較可以得知，第一組的gif(第一張圖片與第一、二張align後的圖片所產生的gif)表現的效果比起其他兩組還要好。

##  Image processing to enhance effect
此部份吾組採用的方法即是讓上述曾提及的第一二、第一三以及第一四這三張alignment後的圖片的結果不會有黑色像素產生，進而讓後面製作gif的時候能增強Motion parallax的效果。而們實作的細節就是擷取我們要的圖片內容範圍->去除黑色像素的部分->最後在resize成800 * 900，而這樣alignment後的圖片就不會有黑色像素的生成!<br><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/12/re_12.gif" width="500" height="500">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/13/re_13.gif" width="500" height="500">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/14/re_14.gif" width="500" height="500">

## 3 different effects

