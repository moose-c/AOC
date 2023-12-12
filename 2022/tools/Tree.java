package tools;

import java.util.Map;
import java.util.Objects;
import java.util.HashMap;
import java.util.ArrayList;
import java.util.Collection;

public class Tree {
    private class Leaf {
        public ArrayList<Leaf> children = new ArrayList<Leaf>();
        public String name;
        public Leaf parent;
        public int value;

    public Leaf(String name_str) {
        name = name_str; 
        value = 0;
        }

    public Leaf(String name_inp, Leaf parent_inp) {
        name = name_inp;
        parent = parent_inp;
        value = 0;
        }

    public void addChild(Leaf child) {
            children.add(child);
        }
    }

    Leaf current_location;
    Map<String, Leaf> structure = new HashMap<String, Leaf>();

    public Tree(String root_name) {
        Leaf root = new Leaf(root_name);
        structure.put("root", root);
        current_location = root;
    }

    public void traverseTree(String name_new_location){
        Leaf new_location = structure.get(name_new_location);
        current_location = new_location;
    }

    public void backtrack() {
        current_location = current_location.parent;
    }

    public void addChild(String name){
        Leaf child = new Leaf(name, current_location);
        current_location.addChild(child);
        structure.put(child.name, child);
    }

    public void updateValue(int additional_value) {
        current_location.value += additional_value;
        if (! (Objects.isNull(current_location.parent))) {
            Leaf old_location = current_location;
            current_location = current_location.parent;
            updateValue(additional_value); 
            current_location = old_location;
        }        
    }
    
    public int obtainResult(){
        Collection<Leaf> leaves = structure.values();

        int count = 0;
        for (Leaf leaf : leaves) {
            if (leaf.value <= 100000) count+=leaf.value;
        }

        return count;
    }
}
