// we import this to access the Scanner class
import java.util.Scanner;

class Main {

// This is the main method where we can call functions
  public static void main(String[] args) {
    long startTime = System.currentTimeMillis();
    System.out.println(System.currentTimeMillis());


    // n is a Scanner object
    Scanner n = new Scanner(System.in);

    System.out.println(
        "Welcome to Battleship! Your objective is to sink all of the enemy's ships."
         + "There's one 2-spaced ship and one 3-spaced ship hidden below the surface."
    );
    System.out.println();

    // Here we create a grid of 10 by 10 where each tile is a bool
    int[][] gridLayout = new int[10][10];
    for (int i = 0; i<gridLayout.length; i++) {
      for (int j = 0; j<gridLayout[i].length; j++) {
        gridLayout[i][j] = 0;
      }
    }

    System.out.println(gridLayout);

    // Print the grid
    layout(gridLayout);

    double numberOfTry = 0.0;
    double numberOfHits = 0.0;
    // number of ships on the board
    int numberOfSquares = 5;

    // Create the grid where the ships can be placed (same as the gridLayout)
    boolean[][] shipArray = new boolean[10][10];

    // One random position on the grid
    // Start point of the ships
    int randStartRow = (int) (Math.random() * 9);
    int randStartCol = (int) (Math.random() * 9);
    int storeShip1Row = (int) (Math.random() * 9);
    int storeShip1Col = (int) (Math.random() * 9);

    // Set the tile that storeShip1 and storShip2 are on to true
    shipArray[storeShip1Row][randStartCol] = true;
    shipArray[randStartRow][storeShip1Col] = true;

    // Check if the storeShip1Row is on on row 9: If it is then add another ship
    // that is 1 to the left and set that tile to true ; if not then add a ship 1 to
    // the right and set that tile to true (Note: the storeShip1Row is 2 tiles long)
    if (storeShip1Row == 9) {
      storeShip1Row--;
      shipArray[storeShip1Row][randStartCol] = true;
    } else {
      storeShip1Row++;
      shipArray[storeShip1Row][randStartCol] = true;
    }

    // Check if the storeShip1Col is on the 9th tile: if it is not then add 3 ships
    // down and set all to true else add 3 ships up and set them to true
    if (storeShip1Col + 3 <= 9) {
      shipArray[randStartRow][storeShip1Col + 1] = true;
      shipArray[randStartRow][storeShip1Col + 2] = true;
    } else {
      shipArray[randStartRow][storeShip1Col - 1] = true;
      shipArray[randStartRow][storeShip1Col - 2] = true;
    }
    

    /*
     * Check if the user hits all of the ships equal to the numberOfSquares
     * (which is the number of ships).
     * While the numberOfHits is not equal to numberOfSqaures,
     * then keep printing the user inputs of row and column
     */
    while (numberOfHits != numberOfSquares) {
      System.out.println();
      System.out.print("Pick a row: ");
      int rowInput = n.nextInt();
      System.out.print("Pick a column: ");
      int columnInput = n.nextInt();

      // Checks if the user inputs are in bound from 0 to 9
      if (rowInput > 9 || rowInput < 0 || columnInput > 9 || columnInput < 0) {
        System.out.println("Input not allowed in grid. Please try again");
        System.out.print("Pick a row: ");
        rowInput = n.nextInt();
        System.out.print("Pick a column: ");
        columnInput = n.nextInt();
      }
      
      // Checks if the rowInput and columInput hit a ship on the shipArray grid and
      // not the gridLayout
      if (shipArray[rowInput][columnInput]) {
        System.out.println("It's a hit! ");
        // Increase numberOfHits everytime a ship is hit
        numberOfHits += 1;
        // Set the tile on the gridLayout to true(same spot where the ship is)
        gridLayout[rowInput][columnInput] = 2;
        // print a new grid with all of the new information
        layout(gridLayout);
        // else statment that checks if you already have a hit on that spot
      }

      // if condition for missing
      if (!shipArray[rowInput][columnInput]) {
        System.out.println("It's a miss!");
        gridLayout[rowInput][columnInput] = 1;
        layout(gridLayout);
        // Always increase numberOfTry everytime you miss
        numberOfTry++;

        gridLayout[rowInput][columnInput] = 1;
      }

      // check if we won (Hint: this is the final part of the program)
      if (numberOfHits == numberOfSquares) {
        
        // breaks the loops
        break;
      }
    }
    System.out.println("Congratulations! Your hit percentage was: " + (100*((numberOfHits/(numberOfHits+numberOfTry)))) + "%!\nThe total guesses you took were: " + (numberOfHits+numberOfTry) + "!\nYour overall time was: " + (System.currentTimeMillis()-startTime)/60000 + " minutes!");
  }

  // function that creates the board evertime until you win
  public static void layout(int[][] gridLayout) {
    int storeNumOut = 0;
    // prints the row and column numbers
    System.out.print("  0 1 2 3 4 5 6 7 8 9");

    // Nested for loop that prints the board
    for (int r = 0; r < gridLayout.length; r++) {
      // These lines print the numbers of the columns by starting
      // each row with a number
      System.out.println();
      System.out.print(storeNumOut);
      storeNumOut += 1;

      /*
       * Checks if the tile is true or false: by default all tiles are false
       * (Note: This allows the next board that is printed to have the "-" and
       * "x" in the spot that is a hit or miss from the previous attempt)
       */
      for (int c = 0; c < gridLayout[r].length; c++) {
        // if statement that marks "-" if tile false and "x" if tile is true
        // (Note: Tiles that are true are the tiles that have ships on them)
        if (gridLayout[r][c] == 0) {
          System.out.print(" - ");
        } else if (gridLayout[r][c] == 1) {
          System.out.print("\u001B[31m"+" O "+"\u001B[37m	");
        } else if (gridLayout[r][c] == 2) {
          System.out.print("\u001B[32m" + " X " + "\u001B[37m");
        }
      }
    }
    System.out.println();
  }
}