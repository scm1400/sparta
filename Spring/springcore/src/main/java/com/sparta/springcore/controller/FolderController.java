package com.sparta.springcore.controller;
import com.sparta.springcore.dto.FolderCreateRequestDto;
import com.sparta.springcore.domain.Folder;
import com.sparta.springcore.exception.ApiException;
import com.sparta.springcore.security.UserDetailsImpl;
import com.sparta.springcore.service.FolderService;
import lombok.RequiredArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RequiredArgsConstructor
@RestController
public class FolderController {
    // 멤버 변수 선언
    private final FolderService folderService;

    // 회원이 등록한 모든 폴더 조회
    @GetMapping("/api/folders")
    public List<Folder> getFolders(@AuthenticationPrincipal UserDetailsImpl userDetails) {
        return folderService.getFolders(userDetails.getUser());
    }

    // 회원이 폴더 추가
    @PostMapping("/api/folders")
    public List<Folder> addFolders(@RequestBody FolderCreateRequestDto folderCreateRequestDto, @AuthenticationPrincipal UserDetailsImpl userDetails) {
        List<String> folderNames = folderCreateRequestDto.getFolderNames();
        return folderService.createFolders(folderNames, userDetails.getUser());
    }

    @ExceptionHandler({ IllegalArgumentException.class })
    public ResponseEntity<Object> handle(IllegalArgumentException ex) {
        ApiException apiException = new ApiException(
                ex.getMessage(),
                // HTTP 400 -> Client Error
                HttpStatus.BAD_REQUEST
        );

        return new ResponseEntity<>(
                apiException,
                HttpStatus.BAD_REQUEST
        );
    }
}