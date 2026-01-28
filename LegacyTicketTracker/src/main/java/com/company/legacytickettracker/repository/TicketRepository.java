package com.company.legacytickettracker.repository;

import com.company.legacytickettracker.model.Ticket;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TicketRepository extends JpaRepository<Ticket, Long> {
}
