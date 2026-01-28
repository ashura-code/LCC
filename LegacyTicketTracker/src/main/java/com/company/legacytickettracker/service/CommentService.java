package com.company.legacytickettracker.service;

import com.company.legacytickettracker.model.Comment;
import com.company.legacytickettracker.repository.CommentRepository;
import org.springframework.stereotype.Service;

@Service
public class CommentService {

    private final CommentRepository repo;

    public CommentService(CommentRepository repo) {
        this.repo = repo;
    }

    public Comment create(Comment c) {
        return repo.save(c);
    }
}
