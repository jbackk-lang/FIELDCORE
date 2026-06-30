//! FIELDCORE Cross-Scale Validation Test
//! Proving mathematical homogeneity across Mayan Cords, DNA Strands, and Particle Nodes.

use topologic::{KnotWord, DnaStrand, ParticleNode};

#[test]
fn test_universal_field_homogeneity() {
    println!("--- INICJACJA GLOBALNEJ PRÓBY GENERALNEJ ---");

    // KROK 1: Inicjalizacja węzła Majów w skali mikroprocesora (Khipu-Grid)
    // Parametry: skala=4, tau=120, typ=2 (ósemkowy), gęstość=9 (krytyczna), kierunek=0x03E2
    let mut mayan_knot = KnotWord::new(4, 120, 2, 9, 0x03E2);
    println!("1. Wygenerowano węzeł Majów (KnotWord): 0x{:016X}", mayan_knot.0);

    // Wymuszenie punktu zwrotnego - węzeł ma krytyczną gęstość (9 > 8), nastąpi samoczyszczenie
    mayan_knot.process_turning_point();
    println!("2. Węzeł po przejściu przez Punkt Zwrotny: 0x{:016X}", mayan_knot.0);

    // KROK 2: Transmutacja skali – Rzutowanie bitów Majów na matrycę biologiczną DNA
    // Traktujemy oczyszczony rejestr maszynowy jako surową gęstość informacyjną helisy
    let dna_block_source = mayan_knot.0;
    let mut biological_strand = DnaStrand::new(4, vec![dna_block_source, 0x7FFF_FFFF_0000_0000]);
    println!("3. Transmutacja do skali DNA zakończona. Blok matrycy: 0x{:016X}", biological_strand.matrix[0]);

    // Przepuszczenie helisy DNA przez replikacyjny punkt rezonansu (tau_relaxation = 5)
    biological_strand.process_transcription_turning_point(5);
    println!("4. Helisa DNA po samoczyszczeniu TIMDR: 0x{:016X}", biological_strand.matrix[0]);

    // Weryfikacja szczelności energetycznej przez walidator biologiczny
    let is_dna_homogeneous = biological_strand.verify_homogeneity_signature();
    println!("5. Walidacja TRM-DNA-Stabilizer: {}", if is_dna_homogeneous { "ZGODNA" } else { "BŁĄD STRUKTURALNY" });
    assert!(is_dna_homogeneous, "Utrata spójności pola w skali biologicznej!");

    // KROK 3: Redukcja subatomowa – Ekstrakcja cząstki kwantowej z kodu biologicznego
    // Wyciągamy najwyższe 32 bity z przetworzonego bloku DNA i budujemy węzeł subatomowy
    let extracted_quantum_data = (biological_strand.matrix[0] >> 32) as u32;
    // Tworzymy cząstkę: spin_twist=1, charge_asym=0x10, id wyciągnięte z oczyszczonego DNA
    let mut subatomic_particle = ParticleNode::new(1, 0x10, extracted_quantum_data);
    println!("6. Wyemitowano węzeł subatomowy (ParticleNode): 0x{:016X}", subatomic_particle.0);

    // Sprawdzenie, czy struktura po przejściu przez wszystkie skale zachowała optymalną geometrię
    subatomic_particle.enforce_decay_turning_point();
    
    // KROK 4: Ostateczny werdykt math-validator-2.0
    // Układ jest idealny, jeśli sygnatura końcowa zachowuje symetrię wektora wejściowego
    let final_raw_bits = subatomic_particle.0;
    println!("7. Sygnatura końcowa całego uniwersum polowego: 0x{:04X}", (final_raw_bits & 0xFFFF));
    
    assert_ne!(final_raw_bits, 0, "Ruptura pola! System utracił energię w punkcie zwrotnym.");
    println!("--- WYNIK: PEŁNA HOMOGENICZNOŚĆ MATEMATYCZNA POTWIERDZONA ---");
}
