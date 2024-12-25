use std::collections::HashMap;
use std::fs;

use counter::Counter;

fn path_from_to<'a>(fr: char, to: char, pad_num: i32) -> String {
    let pad: HashMap<char, (i32, i32)>;
    if pad_num == 0 {
        pad = HashMap::from([
            ('9', (2, 0)),
            ('8', (1, 0)),
            ('7', (0, 0)),
            ('6', (2, 1)),
            ('5', (1, 1)),
            ('4', (0, 1)),
            ('3', (2, 2)),
            ('2', (1, 2)),
            ('1', (0, 2)),
            ('0', (1, 3)),
            ('A', (2, 3)),
            ('.', (0, 3)),
        ]);
    } else {
        pad = HashMap::from([
            ('^', (1, 0)),
            ('A', (2, 0)),
            ('<', (0, 1)),
            ('v', (1, 1)),
            ('>', (2, 1)),
            ('.', (0, 0)),
        ]);
    }

    if fr == to {
        return String::from("A");
    }

    let from_pos = pad.get(&fr).unwrap();
    let to_pos = pad.get(&to).unwrap();
    let dx = to_pos.0 - from_pos.0;
    let dy = to_pos.1 - from_pos.1;
    let horizontal = if dx < 0 {
        "<".repeat(dx.wrapping_abs() as usize)
    } else if dx > 0 {
        ">".repeat(dx.wrapping_abs() as usize)
    } else {
        String::new()
    };
    let vertical = if dy < 0 {
        "^".repeat(dy.wrapping_abs() as usize)
    } else if dy > 0 {
        "v".repeat(dy.wrapping_abs() as usize)
    } else {
        String::new()
    };

    if dx == 0 {
        return vertical + "A";
    }
    if dy == 0 {
        return horizontal + "A";
    }

    let dead = *pad.get(&'.').unwrap();
    if dx > 0 && (dead.0 != from_pos.0 || dead.1 != to_pos.1) {
        return vertical + &horizontal + "A";
    }
    if dead.0 != to_pos.0 || dead.1 != from_pos.1 {
        return horizontal + &vertical + "A";
    }

    return vertical + &horizontal + "A";
}

fn get_path<'a>(code_counter: Counter<String, usize>, pad: i32) -> Counter<String, usize> {
    let mut new_counter: Counter<String, usize> = Counter::new();
    for (code, count) in code_counter {
        let mut sym = 'A';
        for c in code.chars() {
            let path = path_from_to(sym, c, pad);
            new_counter[&path] += count;
            sym = c;
        }
    }

    new_counter
}

fn main() {
    let codes = fs::read_to_string("../input.txt").expect("Should have been able to read the file");
    let codes = codes.split_whitespace();
    let mut total = 0;
    for code in codes {
        let mut code_counter: Counter<String, usize> = Counter::new();
        code_counter[&String::from(code)] = 1;
        let mut path = get_path(code_counter, 0);
        for _i in 0..25 {
            path = get_path(path, 1);
        }
        let numeric_code = code
            .chars()
            .filter(|c| c.is_numeric())
            .collect::<String>()
            .parse::<usize>()
            .unwrap();
        let path_length: usize = path.keys().map(|k| k.len() * path.get(k).unwrap()).sum();
        total += path_length * numeric_code;
    }

    println!("{}", total)
}
