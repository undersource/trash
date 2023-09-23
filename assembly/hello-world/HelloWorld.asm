format ELF64 executable
entry _start

msg db "Hello world!", 0xA, 0
len = $-msg

_start:
    mov rax, msg
    call print_string
    call exit

; | input:
; rax = string
print_string:
    push rax
    push rbx
    push rcx
    push rdx
    mov rcx, rax
    call length_string
    mov rdx, rax
    mov rax, 4 ; 4 - write
    mov rbx, 1 ; 1 - stdout
    int 0x80
    pop rdx
    pop rcx
    pop rbx
    pop rax
    ret

; | input:
; rax = string
; | output:
; rax = length
length_string:
    push rdx
    xor rdx, rdx
    .next_iter:
        cmp [rax+rdx], byte 0
        je .close
        inc rdx
        jmp .next_iter
    .close:
        mov rax, rdx
        pop rdx
        ret

exit:
    mov rax, 1 ; 1 - exit
    mov rbx, 0 ; 0 - return
    int 0x80
