fn blink(stone: u128) -> Vec<u128> {
    if stone == 0 {
        return [1].to_vec();
    } else if stone.to_string().len() % 2 == 0 {
        let s = stone.to_string();
        return [
            s[..(s.len() / 2)].parse::<u128>().unwrap(),
            s[(s.len() / 2)..].parse::<u128>().unwrap(),
        ]
        .to_vec();
    } else {
        return [stone * 2024].to_vec();
    }
}

fn main() {
    let mut stones: Vec<u128> = [4022724, 951333, 0, 21633, 5857, 97, 702, 6].to_vec();

    for i in 0..75 {
        println!("{:?}", i);
        let mut new_stones: Vec<u128> = vec![];
        for s in &stones {
            new_stones.append(&mut blink(*s));
        }

        stones = new_stones;
    }

    println!("{:?}", stones.len());
}
