import javafx.application.Application;
import javafx.stage.Stage;
import javafx.scene.Scene;
import javafx.scene.layout.GridPane;
import javafx.scene.text.Text;
import javafx.scene.control.Label;
import javafx.scene.control.TextField;
import javafx.scene.control.Button;
import javafx.event.ActionEvent;
import javafx.geometry.Pos;
import javafx.geometry.HPos;
import java.io.IOException;
import javafx.scene.control.Alert;
import java.lang.ProcessBuilder;

public class RomanToDecimalConverter extends Application{

    private TextField romanField;
    private TextField decimalField;
    private Label romanLabel;
    private Label decimalLabel;
    private Button romanToDec;
    private Button decToRoman;
    private Button clear;

    public void start(Stage primaryStage){
        primaryStage.setTitle("Roman Decimal Converter App");

        romanField = new TextField();
        romanField.setPrefWidth(200);
        decimalField = new TextField();
        decimalField.setPrefWidth(200);

        romanLabel = new Label("Roman Numeral: ");
        decimalLabel = new Label("Decimal Number: ");

        romanToDec = new Button("Convert To Decimal");
        romanToDec.setOnAction(this::romeToDecConvert);
        decToRoman = new Button("Convert To Roman");
        decToRoman.setOnAction(this::decToRomanConvert);

        clear = new Button("Clear Both Fields");
        clear.setOnAction(this::clearFields);

        GridPane myPane = new GridPane();

        myPane.setAlignment(Pos.CENTER);
        GridPane.setHalignment(clear, HPos.CENTER);
        myPane.setHgap(20);
        myPane.setVgap(20);

        myPane.add(romanLabel, 0, 0);
        myPane.add(romanField, 1, 0);
        myPane.add(romanToDec, 2, 0);
        myPane.add(decimalLabel, 0, 1);
        myPane.add(decimalField, 1, 1);
        myPane.add(decToRoman, 2, 1);
        myPane.add(clear, 1, 2);

        Scene myScene = new Scene(myPane, 500, 200);

        primaryStage.setScene(myScene);
        primaryStage.show();

    }

    public void romeToDecConvert(ActionEvent event){
        
        String romanNumeral = romanField.getText().toUpperCase();
        romanNumeral = romanNumeral.trim();
        if(romanNumeral.length() == 0){
            showError("Input cannot be empty.");
            return;
        }

        try{
            romeToDecConvertHelp(romanNumeral);
        }
        catch(IOException ioe){
            showError("Problem with input.");
        }
        catch(InterruptedException ie){
            showError("Interrupted flow.");
        }


    }

    public void decToRomanConvert(ActionEvent event){
        
        String decimal = decimalField.getText();
        decimal = decimal.trim();
        int intDecimal;

        if (decimal.length() == 0){
            showError("Input cannot be empty.");
            return;
        }

        try{
            intDecimal = Integer.parseInt(decimal);
            if (intDecimal < 0){
                showError("Cannot convert negative numbers.");
                decimalField.clear();
                return;
            }
        }

        catch (NumberFormatException nfe){
            showError("You should enter an integer.");
            decimalField.clear();
            return;
        }

        try{
            decToRomanConvertHelp(decimal);
        }
        catch (IOException ioe){
            showError("Problem with input.");
        }
        catch (InterruptedException ie){
            showError("Interrupted flow.");
        }


    }

    public void clearFields(ActionEvent event){
        romanField.clear();
        decimalField.clear();
    }


    private void romeToDecConvertHelp(String input) throws IOException, InterruptedException{
        ProcessBuilder pb = new ProcessBuilder("python", "roman_to_decimal_backend.py", input);
        Process process = pb.start();

        String output = new String (process.getInputStream().readAllBytes());
        output = output.trim();

        String error = new String (process.getErrorStream().readAllBytes());
        error = error.trim();

        int successCode = process.waitFor();

        if(successCode == 0){
            decimalField.setText(output);
        }
        else{
            showError(error);
            romanField.clear();
        }
    }

    private void decToRomanConvertHelp(String input) throws IOException, InterruptedException{
        ProcessBuilder pb = new ProcessBuilder("python", "decimal_to_roman_backend.py", input);
        Process process = pb.start();

        String output = new String (process.getInputStream().readAllBytes());
        output = output.trim();

        String error = new String (process.getErrorStream().readAllBytes());
        error = error.trim();

        int successCode = process.waitFor();

        if (successCode == 0){
            romanField.setText(output);
        }

        else{
            showError(error);
        }


    }

    private void showError(String message){

        Alert alert = new Alert(Alert.AlertType.WARNING);
        alert.setTitle("Error");
        alert.setHeaderText("Invalid Input");
        alert.setContentText(message);
        alert.showAndWait();

    }

}