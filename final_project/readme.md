# How to chat like A Pro
### Chatting Aided System 

Jason Tang, Frank Tsai, Andy Chien

System : https://github.com/ju5td0m7m1nd/chat_aid

<b>Abstract:</b>

現今的社會越來越不善於和陌生人社交，常會發生一段聊天過程不到10句就接不下去的尷尬情形，但往往只需要一句可以破冰的關鍵，就能夠延續一段友誼，甚至是成為知心好友。
當使用交友軟體的人正面臨到「無言」窘境，像是被句點（哈哈、喔喔.....等等）或不知該如何回話等等，本計劃會即時推薦較能延續話題的內容，供使用者參考。
 
<b>Goals of the project:</b>

本研究以通訊軟語料庫為基礎，建構聊天破冰小幫手。小幫手會提供使用者聊天時的話題建議或者接續語句提升聊天軟體的用戶體驗。小幫手的輸入主要為使用者聊天的前幾句紀錄，輸出為若干主題建議或者語句，並且以「話題延續程度」為基準排序。
 
<b>Prblem Statement:</b>

將當前的聊天內容轉成Vectors V (v0, v1, v2, ……, vn-1)丟進train過的model，取得data裡與V相似度較高的片段V’，並得到下一個可以延續聊天內容的句子vn，再將vn轉回原先的句子s呈現給使用者。
 
 
<b>Detailed plan of activities:</b>
 
(1) 剖析資料、資料前處理、分類對話

     1.1 找出聊天記錄的段落
     1.2 區隔男女生聊天的語句
     1.3 算出句子間的向量
     
 (2) Sentences representation
 
     2.1 Tf-Idf vectorization
     2.2 Doc2Vec
     2.3 Average (Median) Word2Vec
     
(3) Mapping Model

     3.1 Parse user’s input
     3.2 get the most similar sentence in model
     3.3 return the following sentence to enhance user’s chat experience.

