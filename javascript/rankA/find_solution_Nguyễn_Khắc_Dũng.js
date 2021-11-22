// Kiem tra xung quanh xem co di duoc tiep hay khong
var checkAround = (positionCol, positionRow, matrix, wordCheck, sizeOfMatrix) => {
  if (matrix[positionRow][positionCol + 1] == wordCheck && positionCol < sizeOfMatrix) {
    return ["true", positionRow, positionCol + 1];
  }

  if (matrix[positionRow][positionCol - 1] == wordCheck && positionCol > 0) {
    return ["true", positionRow, positionCol - 1];
  }

  if (matrix[positionRow + 1][positionCol] == wordCheck && positionRow < sizeOfMatrix) {
    return ["true", positionRow + 1, positionCol];
  }

  if (matrix[positionRow - 1][positionCol] == wordCheck && positionRow > 0) {
    return ["true", positionRow - 1, positionCol];
  }

  return ["false", positionRow, positionCol];
};

// Kiem tra xem co the tao duoc hay khong
var checkStringCreateByMatrix = (sizeOfMatrix, matrix, stringCheck) => {
  for (let row = 0; row < sizeOfMatrix; row++) {
    if (matrix[row].indexOf(stringCheck[0])) {
      for (let col = 0; col < sizeOfMatrix; col++) {
        if (matrix[row][col] == stringCheck[0]) {
          let PositionRow = row;
          let PositionCol = col;
          let flag ;
          let stringIndex = 1;
          do {
            flag = "false";
            [flag, PositionRow, PositionCol] = checkAround(PositionCol,PositionRow,matrix,stringCheck[stringIndex++],sizeOfMatrix);
          } while (flag == "true" && stringIndex < stringCheck.length);
          
          if (flag == "false") {
            return "no";
          } else {
            return "yes";
          }
        }
      }
    }
  }
};

var findPattern = (sizeOfMatrix, dataOfMatrix, stringsCheck) => {
  // Tao ma tran
  let matrix = [];
  let result = [];
  let data = 0;

  for (let row = 0; row < sizeOfMatrix; row++) {
      let dataOfRow =[]
    let i = 0;
    for (let col = 0; col < sizeOfMatrix; col++) {
        dataOfRow.push(dataOfMatrix[data][i++])
    }
    matrix.push(dataOfRow);
    data++;
  }


  //   kiem tra co tao duoc cac chuoi hay khong
  for (let stringIndex = 0; stringIndex < stringsCheck.length; stringIndex++) {
    result.push(
      checkStringCreateByMatrix(sizeOfMatrix, matrix, stringsCheck[stringIndex])
    );
  }

  return result;
};

console.log(findPattern(3, ["abc", "cab", "bca"], ["abc","bca"]));
