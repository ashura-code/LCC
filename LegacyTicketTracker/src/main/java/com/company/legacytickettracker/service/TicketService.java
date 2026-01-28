package com.company.legacytickettracker.service;

import com.company.legacytickettracker.model.Ticket;
import com.company.legacytickettracker.model.TicketStatus;
import com.company.legacytickettracker.repository.TicketRepository;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TicketService {

    private final TicketRepository repo;

    public TicketService(TicketRepository repo) {
        this.repo = repo;
    }

    public List<Ticket> getAll() {
        return repo.findAll();
    }

    public Ticket create(Ticket t) {
        return repo.save(t);
    }

    public Ticket updateStatus(Long id, TicketStatus status) {
        Ticket ticket = repo.findById(id).orElse(null);
        if (ticket == null) return null;

        ticket.setStatus(status);
        return repo.save(ticket);
    }
}
