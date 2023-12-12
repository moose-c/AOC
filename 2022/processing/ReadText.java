package processing;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ReadText {
    public String[] data;
    public ReadText(){
        data = text_reader("input.txt");
    }
    public ReadText(String filename) {
        data = text_reader(filename);
    }


    public static String[] text_reader(String filename) {
        String[] data = {};
        File input = new File(filename);
        try {
            Scanner scanner = new Scanner(input);
            while (scanner.hasNextLine()) {
                String[] newdata = new String[data.length+1];
                for (int i=0; i < data.length; i++) {
                    newdata[i] = data[i];                
                }
                newdata[newdata.length-1] = scanner.nextLine();
                data = newdata.clone();
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            System.out.println("An error occurred");
            e.printStackTrace();
        }
        return data;
    }
}