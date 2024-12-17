fn main() {
    let program = [2, 4, 1, 1, 7, 5, 4, 4, 1, 4, 0, 3, 5, 5, 3, 0];
    let mut a = 46337277;
    for a0 in 8_u64.pow(15)..8_u64.pow(16) {
        let mut a = a0;
        if a0 % 10000000000 == 0 {
            println!("{}", a0)
        }
        for i in 0..16 {
            let val = a & 0b111 ^ 0b101 ^ (a >> (a & 0b111 ^ 1)) & 0b111;
            a >>= 0b11;

            if val != program[i] {
                break;
            }
            if i == 15 {
                println!("{}", a0);
            }
        }
        if a == 0 {
            println!("{}", a0)
        }
    }

    while a != 0 {
        print!("{},", a & 0b111 ^ 0b101 ^ (a >> (a & 0b111 ^ 1)) & 0b111);
        a >>= 0b11;
    }
}
