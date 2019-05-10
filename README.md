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

由上圖3張matching的結果，可以看出我們兩張不同的圖片feature最相近的部分皆有坐落下鴨子的身體部份上(吾組有用調整程式的參數好讓matching的線皆坐落於鴨子身上，而這用意在於避免alignment後的圖片會有過度變形失真抑或是偏移的情況)。然而從三張alignment的結果可以看出，第一、二張aligment的圖片結果比起第一、三張以及第一、四張的結果來說，呈現的結果還要好(即alignment後的圖片黑色部分較少)，吾組推測這其中的在於位移量的影響。為何吾組會這樣說呢，因為第一、二張圖片的拍攝的位移量比起其他第一、三張圖片以及第一、四張圖片的位移量來說是最小的，所以才會導致這樣的結果。<                                                                                                                      

## Multi-view 3D visual effects
test<br><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/12/12.gif" width="500" height="500">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/13/13.gif" width="500" height="500">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/14/14.gif" width="500" height="500">

##  Image processing to enhance effect
test<br><br>
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/12/re_12.gif" width="500" height="500">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/13/re_13.gif" width="500" height="500">
<img src="https://github.com/TingWeiHuang22/homework5/blob/master/picture/14/re_14.gif" width="500" height="500">

## 3 different effects

