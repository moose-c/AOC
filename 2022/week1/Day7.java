package week1;

import processing.ReadText;
import tools.Tree;


public class Day7 {
    public static void main(String[] args) {
        ReadText reader = new ReadText("input.txt");
        String[] all_data = reader.data;
        String[] data = new String[all_data.length-1];
        System.arraycopy(all_data, 1, data, 0, all_data.length-1);
        Tree final_tree = tree_creation(data);
        System.out.println(final_tree.obtainResult());
    }
    
    static Tree tree_creation(String[] data){
        Tree tree = new Tree("/");
        String[] split_str;

        for (String string : data) {
            split_str = string.split(" ");
            if (split_str[1].equals("cd")){
                if (split_str[2].equals("..")){
                    tree.backtrack();
                } else {
                    tree.traverseTree(split_str[2]);
                }
            } else if (split_str[1].equals("ls")) {
            } else {
                if (split_str[0].equals("dir")){
                    tree.addChild(split_str[1]);
                } 
                else {
                    tree.updateValue(Integer.parseInt(split_str[0]));
                } 
            }
        }
        return tree;
    }
}

