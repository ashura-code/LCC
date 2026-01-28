package com.company.legacytickettracker.controller;

import com.company.legacytickettracker.model.Comment;
import com.company.legacytickettracker.service.CommentService;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/comments")
public class CommentController {

    private final CommentService service;

    public CommentController(CommentService service) {
        this.service = service;
    }

    @PostMapping
    public Comment create(@RequestBody Comment c) {
        return service.create(c);
    }
}
