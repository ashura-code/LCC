package com.company.legacytickettracker.repository;

import com.company.legacytickettracker.model.Comment;
import org.springframework.data.jpa.repository.JpaRepository;

public interface CommentRepository extends JpaRepository<Comment, Long> {
}
