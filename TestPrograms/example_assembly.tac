# we're doing asssembly now
    li 15
    sp GRA
    mov GRA GRB
sc: cin GRB GRB
    sb GRB
    lb GRC
    nand GRC NUL NUL
    jmp sc