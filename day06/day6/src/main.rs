use std::{collections::HashSet, fs};
const SIZE: usize = 130;

fn set_char(s: &mut str, x: usize, y: usize, newchar: char) {
    let idx = y * SIZE + x;
    let s_bytes: &mut [u8] = unsafe { s.as_bytes_mut() };
    assert!(idx < s_bytes.len());
    assert!(s_bytes[idx].is_ascii());
    assert!(newchar.is_ascii());
    // we've made sure this is safe.
    s_bytes[idx] = newchar as u8;
}
fn get_char(s: &str, x: usize, y: usize) -> char {
    s.chars().nth(y * SIZE + x).unwrap()
}

fn main() {
    let contents =
        fs::read_to_string("../input.txt").expect("Should have been able to read the file");

    let mut layout = contents.replace("\n", "");

    let guard_pos = layout.chars().position(|c| c == '^').unwrap();
    let x0 = guard_pos % SIZE;
    let y0 = guard_pos / SIZE;

    let mut count = 0;

    for y_lvl in 0..SIZE {
        println!("{}", y_lvl);
        for x_lvl in 0..SIZE {
            if get_char(&layout, x_lvl, y_lvl) != '.' {
                continue;
            }

            set_char(&mut layout, x_lvl, y_lvl, '#');
            let mut x: isize = x0.try_into().unwrap();
            let mut y: isize = y0.try_into().unwrap();
            let mut dx: isize = 0;
            let mut dy: isize = -1;

            let mut visited = HashSet::new();
            visited.insert((x, y, dx, dy));

            while 0 <= x + dx
                && (x + dx).unsigned_abs() < SIZE
                && 0 <= y + dy
                && (y + dy).unsigned_abs() < SIZE
            {
                if get_char(&layout, (x + dx).unsigned_abs(), (y + dy).unsigned_abs()) == '#' {
                    let t = dx;
                    dx = -dy;
                    dy = t;
                } else {
                    x += dx;
                    y += dy;
                }

                if visited.contains(&(x, y, dx, dy)) {
                    count += 1;
                    break;
                }

                visited.insert((x, y, dx, dy));
            }

            set_char(&mut layout, x_lvl, y_lvl, '.');
        }
    }

    println!("{}", count)
}
