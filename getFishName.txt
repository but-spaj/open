function setDate() {
  // https://qiita.com/kimikimi714/items/19b6a42a8a416f669decから写したコードをベースに、SpreadsheetAppの繰り返しをなくして高速化した
  
  // var start = new Date(); //https://tonari-it.com/gas-spreadsheet-speedup/から時間測定部分を写した行  

  var rawDateColumnIndex = 2; // IFTTTの日時データを保持する列のインデックス
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet(); // bookの指定
  var sheet = spreadsheet.getActiveSheet(); // sheetの指定
  var lastRow = sheet.getLastRow(); // シートのデータのある最終行を取得して変数lastRowに格納
  var arayData = sheet.getRange(2, rawDateColumnIndex, lastRow -1, 1).getValues(); // 2列目の2行目から最終行までを二次元配列arayData[[行1],[行2],[行3],,,[行lastRow-1]]に格納
  // Logger.log("これから配列 " + arayData + " を高速処理します。対象は" + arayData.length + "行あります。" );  
  
  for (var i = 0; i < arayData.length; i++) { // arayDataの長さの直前まで0から1つず順に変数iに格納する間、ブロック内の処理を繰り返す
    var rawDate = arayData[i][0]; // 変数に配列から[行0[列0]~行i[列0]~行arayData-1[列0]]の要素を格納 
    var rawDateValueM = rawDate.toString().slice(-1); // rawDateの要素を文字列に変換したときの末尾を変数rawDateValueMに格納 
    if (rawDateValueM === "M" ) { // rawDataValueMにある文字列右端が"M"、つまりIFTTTの日時データならブロック内の処理を行う
      arayData.splice(i,1,[covertIFTTTDateToGoogleSpreadsheetDate(rawDate)]); // Trueなら、関数convertIFTTT~で変換した日時データをi番目の要素と置換
    }
  }
  sheet.getRange(2, rawDateColumnIndex, arayData.length, 1).setValues(arayData); // arayDataを2列目の2行目から配列の長さまでの範囲に出力
  // Logger.log("以上の処理の結果、配列は " + arayData + " となりました。" );  
  
  // var end = new Date(); //https://tonari-it.com/gas-spreadsheet-speedup/から時間測定部分を写した行
  // var span_sec = (end - start)/1000; //https://tonari-it.com/gas-spreadsheet-speedup/から時間測定部分を写した行
  // Logger.log("処理時間は " + span_sec + " 秒でした。" ); //https://tonari-it.com/gas-spreadsheet-speedup/から時間測定部分を写した行
}

function covertIFTTTDateToGoogleSpreadsheetDate(str) {
  var moment = Moment.moment(str, "MMMM D, YYYY hh:mma"); // strには"September 26, 2017 at 06:52PM"のようなものが入る
  return moment.format("YYYY/MM/DD HH:mm").toString();
}